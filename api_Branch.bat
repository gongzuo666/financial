@echo off
echo 启程财务系统接口自动化运行准备开始......
@echo on


del /f /s /q  E:\songqin\financial\BranchReport\tmp\*.json
del /f /s /q  E:\songqin\financial\BranchReport\tmp\*.jpg
del /f /s /q  E:\songqin\financial\BranchReport\report


@echo off
echo 环境文件删除工作完成，开始运行脚本......
@echo on

cd E:\songqin\financial\testCaseBranch
pytest -sq --alluredir=../BranchReport/tmp
allure generate  ../BranchReport/tmp -o ../BranchReport/report --clean

@echo off
echo 接口自动化运行成功
pause