import abc
from datetime import datetime

class MaxSizeList():
    def __init__(self, value):
        #NOTE: Attributes of class [max length of list and list to which vars are appended]
        self.list = []
        self.value = value

    def push(self, letter):
        self.list.append(letter)
        if len(self.list) > self.value:
            self.list.pop(0)
            return self.list

    def get_list(self):
        return self.list


class WriteFile(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def write(self):
        return
    
    def __init__(self, filename):
        self.filename = filename

    def write_line(self, text):
        fh = open(self.filename, "a") #NOTE: Open file and close file everytime there is a write
        fh.write(text + "\n") #NOTE: Write text to file
        fh.close() #NOTE: Close file

class DelimFile(WriteFile):
    def __init__(self, filename, delim):
        super(DelimFile, self).__init__(filename)
        self.delim = delim
    
    def write(self, this_list):
        line = self.delim.join(this_list)
        self.write_line(line)

class LogFile(WriteFile):
    def write(self, this_line):
        dt = datetime.now()
        date_str = dt.strftime('%Y-%m-%d %H:%M')
        self.write_line('{0}      {1}'.format(date_str, this_line))

class Write_File_new(object):
    def __init__(self, filename, writer):
        self.fh = open(filename, "w") #open file and store file handle
        self.formatter = writer() 

    def write(self, text):
        self.fh.write(self.formatter.format(text))
        self.fh.write('\n')

    def close(self):
        self.fh.close()

class CSVFormatter(object):
    def __init__(self):
        self.delim = ','

    def format(self, this_list):
        new_list = []
        for element in this_list:
            if self.delim in element: #NOTE:Just remove this to unformat
                new_list.append('"{0}"'.format(element))
            else:
                new_list.append(element)
        return self.delim.join(new_list)

class LogFormatter(object):
    def format(self, this_line):
        dt = datetime.now()
        date_str = dt.strftime('%Y-%m-%d %H:%M')
        return "{0}      {1}".format(date_str, this_line)