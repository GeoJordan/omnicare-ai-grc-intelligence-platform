import '@servicenow/sdk/global'

declare global {
    namespace Now {
        namespace Internal {
            interface Keys extends KeysRegistry {
                explicit: {
                    bom_json: {
                        table: 'sys_module'
                        id: '17d1d9d9e0b74aee967c04bf27561d70'
                    }
                    package_json: {
                        table: 'sys_module'
                        id: 'df709fec9adb4c78be4225644a0bf7b2'
                    }
                }
            }
        }
    }
}
