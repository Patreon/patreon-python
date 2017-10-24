import patreon

from my_site import config
from my_site.models.tables import db
from my_site.models.tables.user import User


def update_user_for_tokens(patreon_refresh_token, patreon_access_token):
    # https://www.patreon.com/platform/documentation/oauth -- Step 4
    # Use the tokens to fetch the Patreon profile and pledge data, saving it all to the db.
    api_client = patreon.API(patreon_access_token)
    user_response = api_client.fetch_user()
    user = user_response.data()
    if not (patreon_refresh_token and patreon_access_token and user):
        return None

    db_user = get_or_create_user_for_patreon_user_id(
        patreon_user_data=user,
        patreon_refresh_token=patreon_refresh_token,
        patreon_access_token=patreon_access_token
    )

    pledges = user.relationship('pledges')
    if pledges and len(pledges) > 0:
        pledge = pledges[0]
        db_user.update({
            'patreon_pledge_amount_cents': pledge.attribute('amount_cents')
        })
        db.session.commit()

    return db_user


def get_or_create_user_for_patreon_user_id(patreon_user_data, patreon_refresh_token, patreon_access_token):
    user_id = patreon_user_data.id()
    info = {
        'full_name': patreon_user_data.attribute('full_name'),
        'email': patreon_user_data.attribute('email'),
        'patreon_refresh_token': patreon_refresh_token,
        'patreon_access_token': patreon_access_token
    }
    db_user = User.query.filter(User.patreon_user_id == user_id).first()
    if db_user:
        db_user.update(info)
    else:
        info['patreon_user_id'] = user_id
        db_user_pkey = User.insert(info)[0]
        db_user = User.get(db_user_pkey)
    db.session.commit()
    return db_user
