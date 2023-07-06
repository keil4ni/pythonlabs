# Keilani Li
''' The following coding program counts how many lines and errors there are in a backend error log errorFile and writes
it to a file called reportError.txt'''

try:
    errorFile = open("ErrorLog.txt", "r")
    reportFile = open("reportError.txt", "w")

    try:
        lineCount = 0
        numLines = errorFile.readline()
        while numLines != "":
            if numLines.strip():
                lineCount += 1
            numLines = errorFile.readline()
        reportFile.write('Number of lines in file: %d\n\n' % lineCount)
        print('Number of lines in file: %d\n' % lineCount)

        errorFile.seek(0) # brings pointer back to the start of the file

        errorCount = 0
        for line in errorFile:
            line = line.rstrip()
            if "error" in line:
                reportFile.write('%s\n' % line)
                print(line)
                errorCount += 1
            elif "Error" in line:
                reportFile.write('%s\n' % line)
                print(line)
                errorCount += 1
            elif "ERROR" in line:
                reportFile.write('%s\n' % line)
                print(line)
                errorCount += 1
        reportFile.write('Number of errors in file: %d' % errorCount)
        print('Number of errors in file: %d' % errorCount)

    finally:
        errorFile.close()
        reportFile.close()

except IOError:
    print('File could not be opened.')

'''
Number of lines in file: 108

[Sun Mar  7 21:16:17 2018] [error] [client 24.70.56.49] File does not exist: /home/httpd/twiki/view/Main/WebHome
[Mon Mar  8 07:27:36 2018] [error] [client 61.9.4.61] File does not exist: /usr/local/apache/htdocs/_vti_bin/owssvr.dll
[Mon Mar  8 07:27:37 2018] [error] [client 61.9.4.61] File does not exist: /usr/local/apache/htdocs/MSOffice/cltreq.asp
[Thu Mar 11 02:27:34 2018] [error] [client 200.174.151.3] File does not exist: /usr/local/mailman/archives/public/cipg/2018-november.txt
[Thu Mar 11 07:39:29 2018] [error] [client 140.113.179.131] File does not exist: /usr/local/apache/htdocs/M83A
Number of errors in file: 5

Process finished with exit code 0
'''
