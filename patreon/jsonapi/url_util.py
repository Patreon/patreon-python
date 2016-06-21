from patreon.version_compatibility.urllib_parse import urlencode


def build_url(path, includes=None, fields=None):
    def joined_or_null(arr):
        return "null" if len(arr) == 0 else ','.join(arr)

    connector = '&' if '?' in path else '?'
    params = {}
    if includes:
        params.update({'include': joined_or_null(includes)})
    if fields:
        params.update({
            "fields[{resource_type}]"
            .format(resource_type=resource_type): joined_or_null(attributes)
            for resource_type, attributes in fields.items()
        })
    return "{path}{connector}{encoded_params}".format(
        path=path,
        connector=connector,
        encoded_params=urlencode(params)
    )
