import configparser


class INIParser(configparser.ConfigParser):
    def as_dict(self):
        """

        :return:
        """
        dic = dict(self._sections)

        for key in dic:
            dic = dict(dic[key])
        for key in dic:
            dic[key] = dic[key].split(',')
        return dic

    def get_options(self):
        for sec in self._sections:
            ops = self.options(sec)
            return ops

# cfg = INIParser()
# cfg.read('2018年日历.ini')


