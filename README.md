# Echo

A minimalistic Python wheel that echoes back the arguments passed to it.

## Getting started

1. `pyenv install` if you're using `pyenv` to manage Python versions
2. `script/build` builds the Python module into a wheel
3. `script/deploy` copies the wheel to DBFS using the default `databricks-cli` profile

## Entrypoints

Three entrypoints are defined:

- `echo = echo:main` (takes no arguments and echoes `sys.argv[1:]` back)
- `echo_with_args = echo:main_with_args` (takes `*args, **kwargs` and echoes back everything)
- `parse_with_args = echo:parse_with_args` (takes `*args, **kwargs`, parses with ArgumentParser and echoes back everything)

`echo_with_args` takes optional `*args` and `**kwargs` arguments that can be passed directly.

## Usage

### CLI

```bash
$ python -m echo foo bar
sys.argv[1:] ['foo', 'bar']

$ echo_with_args foo bar
args ()
kwargs {}
sys.argv[1:] ['foo', 'bar']
```

$ parse_with_args --foo=bar --throw=nothing
args Namespace(args=[], throw='nothing')
leftovers ['--foo=bar']

```
### Python

```python
$ python
Python 3.10.3 (main, Apr 19 2022, 18:41:11) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from echo import main_with_args
>>> main_with_args("arg1", "arg2", kwarg1="value1", kwarg2="value2")
args ('arg1', 'arg2')
kwargs {'kwarg1': 'value1', 'kwarg2': 'value2'}
sys.argv[1:] []
```
