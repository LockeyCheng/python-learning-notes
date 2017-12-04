### 1、项目功能

  主要是为 Prometheus 监控和报警生成配置文件以及配置通知选项等，并且这些操作都可以通过web界面进行，只需要遵守一定的数据格式即可。

### 2、项目的整体结构以及功能

2.1 整体结构：

项目是基于Django框架开发，使用Python3；有后端数据库

2.2 功能模块：

Shard：包含多种服务以及多个Prometheus服务器

Service：是Prometheus服务器中指定的监控实例

Projects：Promgen中由服务器利用Exporters和URL端点形成的分组

Farm：一组服务器

Notifiers：用来将（报警通知）信息路由到指定的目标承受体，如电子邮件等

Rule：Prometheus用来进行报警的规则或者说配置

### 3、运行流程

1、通过Promgen提供的web界面生成目标（也就是需要监控的实例对象，如NGINX、MySQL等服务）

2、为目标配置一些监控和报警规则（可配置多个），将目标连同规则下发给Prometheus去工作,由Prometheus根据规则去从目标PULL（抓取）对应的数据信息并进行清洗、分组等操作

3、Prometheus会根据拿到的数据对应报警规则产生一些告警到AlertManager

4、AlertManager将告警进一步处理之后转发给Promgen去处理

5、Promgen会根据之前配置的报警方式发送报警信息到具体载体


### 4、必要的配置

**Promgen配置**

    1.Promgen配置prometheus和alertmanager通信url

    2.Promgen配置config_writer路径用来写入目标配置

    3.Promgen配置rule_writer路径用来写入规则配置，还要指定promtool_path

    4.Promgen配置url_writer路径用来写入url配置

    5.默认的default_exporters以及一些通知选项

**Prometheus配置**

    1.global全局配置

    2.rule_files规则文件路径

    3.alerting告警通信

    4.实例以及实例配置文件

**Alertmanager配置**

    1.route路由
    2.receivers接收通信


参考与学习：

https://github.com/line/promgen

https://line.github.io/promgen/

https://prometheus.io/


使用Prometheus和Grafana监控Mysql服务器性能https://segmentfault.com/a/1190000007040144
