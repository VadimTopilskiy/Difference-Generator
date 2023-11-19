<div align="center">

![picture](https://i.pinimg.com/564x/d3/4e/22/d34e227592c6a2be14f2111978af1183.jpg)

<h1>Difference Generator</h1>

</div>

__"Вычислитель отличий" (gendiff)__ - Это инструмент командной строки для поиска различий между двумя файлами

__"Gendiff"__ - Utility compares two files and shows the difference between them.

### Install:

1. `git clone github.com/VadimTopilskiy/Difference-Generator.git`
2. `make install`
3. `make package-install`

### How to use:
Difference Generator can be used as an **external library** or as **Command Line Interface (CLI) tool**.

### As an external library
```python
from gendiff import generate_diff  
diff = generate_diff(file_path1, file_path2,file_format)
```
### As a Command Line Interface tool

    gendiff [-f file_format] file_path1 file_path2

or

    gendiff [--format file_format] file_path1 file_path2

##### Supported file formats:

* json
* yaml/yml

##### Supported output formats:

* stylish
* plain
* json