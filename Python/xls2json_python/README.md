[[xls2json]]

1、使用前提
    该工具仅支持以下数据类型：
    int  string  bool    float   long    table   sheettype1  sheettype2  sheettype3  sheettype4  sheettype5  language

    其中
    int  string  bool    float   long    table  language为基本数据类型

    sheettype1  sheettype2  sheettype3  sheettype4  sheettype5为嵌套数据类型
    (注：该工具仅支持两层嵌套，即只能在主表中定义嵌套数据类型，而嵌套的数据类型中不能再包含嵌套类型)

    xls表必须包含sheet"主表"

2、工具运行环境：
    python3.6   --确保Python3.6安装成功，在doc命令下执行Python命令成功即可；
    xlrd包   ---在当前目录,cd到xlrd-1.1.0目录下，执行"python setup.py install"

3、input目录为.xls文件存放目录；output为json文件生成目录（注：该文件夹路径不能修改，已在程序中写死）

4、数据类型说明：
    table类型值的三种格式：
    1、table_name = testtable
        table_val = 1,2,3
        输出的json格式为: 
            "testtable":
            [
                1,2,3
            ]
    2、table_name = testtable
        table_val = id=1,name="xiaoming"        ---等号两边不能有空格
        输出的json格式为:
            "testtable":
            [
                {"id":"1","name":"xiaoming"}
            ]
    3、table_name = testtable
        table_val = {id=1,name="xiaoming"},{id=2,name="xiaohong"}   ------中间任何地方不能有空白字符，如：回车等
        输出的json格式为: 
            "testtable":
            [
                {id=1,name="xiaoming"},
                {id=2,name="xiaohong"}
            ]

    1、sheettype1类型：本身为一个table
        该表描述的数据类型为type:xxx, value:xxx， 如：
        "testsheet1":
        [
            {
                "type":"21",
                "value":"0"
            },
            {
                "type":"27",
                "value":"-1467331200000"
            }
        ]
    2、sheettype5类型：
        该类型其实就是sheettype1类型的一个table形式：转成的json示例如下：
        "2":
        [
            [
                {
                    "type":"21",
                    "value":"0"
                }
            ],
            [
                {
                    "type":"21",
                    "value":"111"
                }
            ]
        ]
    3、sheettype2类型：本身为一个对象
        该类型用于描述基本数据类型，格式和sheettype1有所区别，如下：
        "testsheet2":
        {
            "denyStorage":"0",
            "dieMayDropdown":"-1467331200000",
            "offlineDropdown":"哈哈",
            "testtable":
            [
                    {"id":"1","name":"name"}
            ]
        }
    4、sheettype4类型：
        该类型其实就是sheettype2类型的一个table形式：转成的json示例如下：
        "1":
        [
            {
                "tp":"0",
                "n":"3",
                "pro":"4000",
                "testtable":
                [
                    1,2,3
                ]
            },
            {
                "tp":"1",
                "id":"1.4",
                "pro":"呵呵",
                "testtable":
                [
                    {"id":"1","name":"name"},
                    {"id":"2","name":"name2"}
                ]
            }
        ]
    5、sheettype3类型：
        该类型和sheettype4相似，但table里面只含有一个元素；即该表中的id必须唯一
        "1":
        [
            {
                "tp":"0",
                "n":"3",
                "pro":"4000",
                "testtable":
                [
                    1,2,3
                ]
            }
        ]

















