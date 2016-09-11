#!/usr/bin/env python
# encoding: utf-8


"""
@version: 1.0
@author: baoqiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: https://github.com/githubao
@software: PyCharm
@file: test.py
@time: 16-9-8 下午4:17
"""


def main():
    for i in range(0, 11):
        sql = """
        CREATE TABLE `turing_faq_simi_%s` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '自增id',
  `api_key` varchar(32) NOT NULL COMMENT '用户身份',
  `question_id` int(11) unsigned NOT NULL COMMENT '与faq表格对应的问题的id数据',
  `question` varchar(256) NOT NULL COMMENT '问题',
  `new_ques` varchar(256) NOT NULL,
  `segment` varchar(512) DEFAULT NULL COMMENT '问题的原始切词信息',
  `label_id` int(11) NOT NULL DEFAULT '0',
  `state` int(4) NOT NULL DEFAULT '1' COMMENT '1-在线 0-下线',
  `create_time` datetime NOT NULL COMMENT '入库时间',
  `update_time` datetime NOT NULL COMMENT '最后修改时间',
  PRIMARY KEY (`id`),
  KEY `idx_question` (`api_key`,`question`(255),`state`) USING BTREE,
  KEY `idx_newques` (`api_key`,`new_ques`(255),`state`) USING BTREE,
  KEY `for_id%s` (`question_id`),
  CONSTRAINT `for_id%s` FOREIGN KEY (`question_id`) REFERENCES `turing_faq_%s` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COMMENT='faq相似问题表';
        """

        if i < 10:
            i = '0'+str(i)

        sql = sql.replace("%s", str(i))
        print(sql)


if __name__ == '__main__':
    main()
