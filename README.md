# Dynatrace Problem Report Tool
## **Overview** <img src=https://i.imgur.com/geLcjrW.png align=right width=10%>
- This tool help user to use **Dynatrace Problem API** so easily with GUI. You can export problem list in your **Dynatrace** system to an excel report.
## **How to use**
> To use this, you need to configure your setting with some following information. Go to **Options** > **Settings**.
- **Dynatrace URL**
    - To use Dynatrace API, we use GET method with appropriate URL format. Choose 1 in 3 following formats :
        - Managed : `https://{your-domain}/e/{your-environment-id}`
        - SaaS : `https://{your-environment-id}.live.dynatrace.com`
        - ActiveGate : `https://{your-activegate-domain}/e/{your-environment-id}`
- **Token API**
    - We need to creat an API token to authorize with APi. To do that, follow these steps :
        - Select **Settings** in the navigation menu.
        - Go to **Integration** > **Dynatrace API**.
        - Select **Generate token**.
        - Enter a name for your token.
        - Select ***Read problems*** (API v2) permission for the token.
        - Select **Generate**.
        - Copy the generated token to the clipboard. Store the token in a password manager for future use.
-  **Title**
    - Use for title of output Excel file
    - **Ex:** Your title is `DYNATRACE PROBLEM REPORT`. Your output is :

        <img src=https://i.imgur.com/RwJRriZ.png>

- **Output Folder**
    - Use to browse to the folder you want to store output file.
- **File name prefix**
    - Default settings is `problem`. Output file name has following fomat :
        ```
        {file-name-prefix}_{from}_{to}.xlsx
        ````
    - **Ex:** `problem_20210519_20210519.xlsx`

