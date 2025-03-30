# West Debug Tools

A collection of [Zephyr](https://zephyrproject.org/) `west`
[extensions](https://docs.zephyrproject.org/latest/develop/west/extensions.html)
for convenient debugging.

## Install

`west dbt` can be added to any Zephyr project by adding the following to the
`west.yml` manifest file.

```yaml
    - name: west-debug-tools
      revision: main
      url: https://github.com/hasheddan/west-debug-tools
      west-commands: west-commands.yml
```

## Tools

The following tools are currently supported.

### `addr2src`

Emits the file path, line number, and source at the specified address.

```
west dbt addr2src <address>
```
