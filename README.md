#Test with Gabri

1) Count files in directory tree

    $ find src/test/resources/filecount -type f | wc -l
    12

    $ find src/test/resources/minions -type f | wc -l
    62

2) Count lines in directory tree

    $ find src/test/resources/filecount -type f -exec cat {} + | wc -l
    16

    $ find src/test/resources/minions -type f -exec cat {} + | wc -l
    4034

3) Count code/whitespace/comments of Java code in directory tree

    |$ cloc | src/test/resources/minions |
    -----------|---------------------------|---------------|-----------------|---------|
    |Language   |                  files    |      blank    |    comment      |     code|
    ------------|----------------------------|---------------|-----------------|-------
    |Java      |                      39     |       435       |     255       |    1978|

4) Count code/whitespace/comments for given languages in directory tree

