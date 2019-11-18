# integration-testing
Integration testing utility, which is run from an Azure pipeline upon spinning up a cloud instance of an ESRI Portal.

To incorporate into an Azure DevOps pipeline:
1. Click the Azure pipelines link in DevOps
2. Select the 'feature/Integration-Testing' branch. Ensure you are in master
3. If creating a new job, then 'Add an agent job'
4. Set Display name to Integration testing
5. Click the + to 'add Task'
6. Add 3 command line 'cmd' scripts
7. The first command line creates the virtual environment.

Display name = rem create Venv
Script = 
`echo Creating Python virtual environment in root
cd ..
python -m venv env`

8. The second installs the python dependencies

Display name = install python dependencies
Script = 
`echo Setting proxy
set HTTP_PROXY=REMOVED
set HTTPS_PROXY=REMOVED

echo Installing arcgis

cmd /k "cd /d $(System.DefaultWorkingDirectory)\env\Scripts && activate.bat && cd /d $(System.DefaultWorkingDirectory) && python -m pip install --no-cache-dir arcgis"`

9. The third runs pytest

Display name = run pytests

Script = 

`set HTTP_PROXY=REMOVED
set HTTPS_PROXY=REMOVED

echo Running Python Tests
cmd /k "cd /d $(System.DefaultWorkingDirectory)\env\Scripts # enters the venv dir
&& activate.bat # activates the venv
&& cd /d $(System.DefaultWorkingDirectory)\tests_py\ # enters the test dir
&& pytest --verbose --junitxml=$(System.DefaultWorkingDirectory)\py-test-results.xml # runs pytest as a command with output in junitxml`

10. Finally, in addition to the cmd tasks, a Publish Test Results task is added. 
