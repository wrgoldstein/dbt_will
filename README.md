# What is this

A minimal example of how to use the dbt plugin ecosystem

# Dbt plugins??

There's an experimental, undocumented plugin manager: https://github.com/dbt-labs/dbt-core/blob/main/core/dbt/plugins/manager.py#L27-L31

Note the docstring:

```python
    class dbtPlugin:
        """
        EXPERIMENTAL: dbtPlugin is the base class for creating plugins.
        Its interface is **not** stable and will likely change between dbt-core versions.
        """
```

[This article](https://nicholasyager.com/2023/08/dbt_plugin_api.html) is a helpful introduction.

# How do you use it?

If you `pip install` this package in the same virtualenv as dbt, then runs of dbt will pick up the injected node and act as if it's an allowable ref.

```
$ dbt list
...
dbt_will.will <---- injected
...
```

```sql
select * from {{ ref('will') }} -- compiles to `schema`.`identifier`!
```

