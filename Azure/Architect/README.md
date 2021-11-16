1. Create Virtual Machine
3. Create Storage Account
4. Create Azure SQL Database
    4.1 Create SQL Server
    4.2 Download and install SQL Management Studio - Link to download SQL Management Studio: https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver15
    4.3 Install Visual Studio Community - Link to download Visual Studio Community: https://www.visualstudio.com/en-us/downloads/community-vs.aspx


AZ-304: Design Monitoring and Alerting
[]: # Language: markdown
[]: # Path: Azure\Architect\README.md

1. Azure Monitor -
    - Azure monitor is a cloud-based service that provides visibility into the performance, availability, and security of your Azure resources.
    - Azure monitor provides you with a dashboard that shows you the status of your resources, and alerts you when something unexpected happens.
    - Azure monitor is a free service that you can use to monitor your Azure resources.
    - Create Metrics for your resources
    - Create Alerts for your resources
        - Alerts are triggered when a resource is in an unhealthy state.
        - When an alert is triggered, you can take action to correct the problem.
        - CPU and memory usage is an example of a resource that can be monitored.
        - You can also monitor other resources, such as storage accounts, virtual machines, and databases.
        - You can also monitor your network traffic, and your network security rules.
        - Create Action Groups to define what actions to take when an alert is triggered.
        - You can also create custom actions to perform actions such as sending an email, sending a notification to a chat channel, or performing a webhook.

    - Create Rules for your resources
    - Pin to Dashboard
    - Create Dashboards

    - Activity logs for your resources
        - download the activity log as a CSV file
        - stream log to a Log Analytics Workspace

2. Log Analytics Workspace - 
    - Log Analytics is a cloud-based service that provides you with a centralized view of your data.
    - Log Analytics is a free service that you can use to monitor your Azure resources.
    - 
    - Create Log Analytics Workspace
        - In the Log Analytics Workspace, in workspace data sources.
        - you can connect a resource to a Log Analytics Workspace. like a VM, a storage account, system center, activity logs, etc.
        - To connect, select a data source and click Connect.
          - This will install the Log Analytics agent on the resource.
            - The Log Analytics agent will collect logs from the resource and send them to the Log Analytics Workspace.
        - To select the data you want to send to Log Analytics
         - In the Log Analytics Workspace, in settings
         - Select the Agent Configuration 
            - Select the data you want to send to Log Analytics.
                - for example, you can select event logs, performance counters, IIS logs, etc.

3. Network Security Group Flow logs
    - Network Security Group Flow logs are a way to monitor network traffic.
    - Enable NSG Flow logs, using Network watcher service
        - You will see a list of NSGs, select the NSG you want to monitor.
        - In the flow log settings page, select ON. 
        - Flow Logs version 2 is the latest version. ingress and egress IP traffic for both allowed and blocked traffic.
          - and additional throughput metrics (bytes and packets) per flow. 
        - Select Storage Account.
        - Select the storage account you want to use for the flow logs.
        - Select the retention policy.
    - Traffic Analytics - 
        - Enable Traffic Analysis in the Network Watcher service, using the Network Security Group Flow logs.
        - in the Flow Logs settings page, in the Traffic Analysis section, select ON.
        - Select the Log Analytics workspace.
          - The traffic analysis will be sent to the Log Analytics workspace.
            - If you don't have a Log Analytics workspace, you can create one. 
        - Select the processing analytics interval.
        - in Traffic Analytics section.
            - You can visualize the traffic analysis in the Log Analytics workspace.
            - including malicious traffic, blocked traffic, total traffic, and frequent conversation. 

4. Service Map
    - Service Map is a service that enables you to work with the data stored in your Log Analytics workspace.
    - In the Log Analytics workspace, select Worspace Summary, click Add, and search for the service map.
    - select the  log analytics workspace, and click create. 
    - Set-AzVMExtension -ExtensionName "Microsoft.Azure.Monitoring.DependencyAgent" -ResourceGroupName "new-grp" -VMName "demovm" -Publisher "Microsoft.Azure.Monitoring.DependencyAgent" -ExtensionType "DependencyAgentWindows" -TypeHandlerVersion 9.5 -Location NorthEurope

5. Azure SQL Diagnotics
    - Go to Azure AD, and under the Monitoring section, select Diagnostics settings.
    - Select the logs that you want to send to Log analytics.
    - in order to go ahead and export, the sign in data, your organization needs to have their Azure AD P1 or P2 licenses in place. so you could go ahead and give a setting.

6. Azure AD Sign-ins
    - Select the SQL resource, and under the Monitoring section, select Diagnostics settings.
    - Select the logs that you want to send to Log analytics.

1. Learn Application Insights
2. Learn Azure Sentinel -
   2.1 SIEM - Link to learn Azure Sentinel: https://docs.microsoft.com/en-us/azure/security-insights/security-insights-overview
   2.2 SOAR - Security Orchestration automated response - Link to learn SOAR: https://docs.microsoft.com/en-us/azure/security-insights/security-insights-overview

   2.3 Azure Security Center vs Azure Sentinel - Link to learn Azure Sentinel: https://docs.microsoft.com/en-us/azure/security-insights/security-insights-overview