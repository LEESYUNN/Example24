#!/usr/bin/python3
import os
import time
import shutil
import subprocess

global tableauBackupDirectory
tableauBackupDirectory = "/var/opt/tableau/tableau_server/data/tabsvc/files/backups/"


def generateBackupFileFullPath():
    backupExecDay = time.strftime("%Y-%m-%d", time.localtime())
    backupFileName = "tabserver-{}.tsbak".format(backupExecDay)
    return "{}/{}".format(tableauBackupDirectory, backupFileName)


def execTableauMaintenanceBakcupProcess():
    backupCommands = ['tsm', 'maintenance', 'backup', '-d', '-f', 'tabserver']
    outputBytes = subprocess.check_output(backupCommands)
    print(outputBytes.decode('utf-8'))
    # time.sleep(60 * 30)


def backupMainProcess():

    # 0. defineTargetDirectory
    TARGET_DIR = "/home/tableau_backups"

    # 1. backup
    execTableauMaintenanceBakcupProcess()

    # 2. generateBackupFileFullPath
    backupFileFullPath = generateBackupFileFullPath()

    # 3. execMove
    if os.path.exists(backupFileFullPath):
        shutil.move(backupFileFullPath, TARGET_DIR)
        # shutil.copy(backupFileFullPath, TARGET_DIR)


if __name__ == '__main__':
    backupMainProcess()
