import os
from subprocess import check_call, check_output, CalledProcessError

def main():
    """ Installs Python packages listed in any requirements.txt file
    located at root of project.
    """

    # Returns list of all folders / files in "efs" directory.
    projects = os.listdir("/usr/local/airflow/dags/efs/")

    print(f'Projects in efs {projects}')

    for project in projects:

            project_dir = "/usr/local/airflow/dags/efs/" + project

            try:
                # Installs all packages listed in requirements.txt file.
                check_call(["pip3", "install", "-r", f"{project}/requirements.txt"])

                # Opens requirements.txt to print packages that were successfully installed.
                with open(f'{project_dir}/requirements.txt', "r") as txt:
                    requirements = ''
                    for line in txt:
                        requirements += line
                    print(f'\nThe following Python packages have been installed for project "{project}":\n{requirements}')

            except Exception as e:
                print("Error : " + str(e))
