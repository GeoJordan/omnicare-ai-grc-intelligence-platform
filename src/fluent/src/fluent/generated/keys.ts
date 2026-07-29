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
                composite: [
                    {
                        table: 'sys_dictionary'
                        id: '12e9cf8553f541a8823fef16dc54b451'
                        key: {
                            name: 'x_2089324_omnicare_citation_control'
                            element: 'authority_document'
                        }
                    },
                    {
                        table: 'sys_dictionary'
                        id: '178e08efb4d4438d8c0c0f2c2bfa357c'
                        key: {
                            name: 'x_2089324_omnicare_citation_control'
                            element: 'description'
                        }
                    },
                    {
                        table: 'sys_dictionary'
                        id: '23141c25e8794769bd11daedbcd2853c'
                        key: {
                            name: 'x_2089324_omnicare_authority_document'
                            element: 'name'
                        }
                    },
                    {
                        table: 'ua_table_licensing_config'
                        id: '23df2a6b561f46d3bcfe53ff19b6ff1d'
                        key: {
                            name: 'x_2089324_omnicare_authority_document'
                        }
                    },
                    {
                        table: 'sys_dictionary'
                        id: '3027d1fe939f43758f73bbd45528d452'
                        key: {
                            name: 'x_2089324_omnicare_authority_document'
                            element: 'description'
                        }
                    },
                    {
                        table: 'sys_dictionary'
                        id: '36973e6f5c6f40e3a4d350edcb4d2389'
                        key: {
                            name: 'x_2089324_omnicare_authority_document'
                            element: 'framework_id'
                        }
                    },
                    {
                        table: 'sys_dictionary'
                        id: '3fdc990682e3421eb917d8d9ba4113e9'
                        key: {
                            name: 'x_2089324_omnicare_citation_control'
                            element: 'title'
                        }
                    },
                    {
                        table: 'sys_documentation'
                        id: '41dc4af548034e829b8b7da6cfc980e4'
                        key: {
                            name: 'x_2089324_omnicare_citation_control'
                            element: 'description'
                            language: 'en'
                        }
                    },
                    {
                        table: 'sys_documentation'
                        id: '50d0752c2d344e36b1d885a3d797dfbb'
                        key: {
                            name: 'x_2089324_omnicare_authority_document'
                            element: 'description'
                            language: 'en'
                        }
                    },
                    {
                        table: 'sys_dictionary'
                        id: '65214a1c9e774f2b996ff5a6cbc644d5'
                        key: {
                            name: 'x_2089324_omnicare_authority_document'
                            element: 'NULL'
                        }
                    },
                    {
                        table: 'sys_documentation'
                        id: '7b86e0555cf544b190244edbddcfcd41'
                        key: {
                            name: 'x_2089324_omnicare_citation_control'
                            element: 'authority_document'
                            language: 'en'
                        }
                    },
                    {
                        table: 'sys_documentation'
                        id: '8339fbc856944c4da64569f5f59b912a'
                        key: {
                            name: 'x_2089324_omnicare_authority_document'
                            element: 'framework_id'
                            language: 'en'
                        }
                    },
                    {
                        table: 'sys_documentation'
                        id: '8fa34232e7a4434a8aaa1ea983e4a3cd'
                        key: {
                            name: 'x_2089324_omnicare_authority_document'
                            element: 'name'
                            language: 'en'
                        }
                    },
                    {
                        table: 'sys_documentation'
                        id: '99f8294d38da4657b5864770f4d5dcc6'
                        key: {
                            name: 'x_2089324_omnicare_authority_document'
                            element: 'NULL'
                            language: 'en'
                        }
                    },
                    {
                        table: 'sys_documentation'
                        id: 'a772a328004d4a6485289c4048347fc8'
                        key: {
                            name: 'x_2089324_omnicare_citation_control'
                            element: 'citation_id'
                            language: 'en'
                        }
                    },
                    {
                        table: 'ua_table_licensing_config'
                        id: 'afe84e5111534dd299d8ed9db849b0f3'
                        key: {
                            name: 'x_2089324_omnicare_citation_control'
                        }
                    },
                    {
                        table: 'sys_db_object'
                        id: 'b34bc9f710c247b7868dfdce0bcb216e'
                        key: {
                            name: 'x_2089324_omnicare_citation_control'
                        }
                    },
                    {
                        table: 'sys_documentation'
                        id: 'd3de5fa34cbd4e6a8508d2057ee117d0'
                        key: {
                            name: 'x_2089324_omnicare_citation_control'
                            element: 'NULL'
                            language: 'en'
                        }
                    },
                    {
                        table: 'sys_dictionary'
                        id: 'd7395df27fca4ebdb47434bf857a7e3e'
                        key: {
                            name: 'x_2089324_omnicare_citation_control'
                            element: 'citation_id'
                        }
                    },
                    {
                        table: 'sys_db_object'
                        id: 'e07aa47c325e4ccdb2e1e9d60239a4e0'
                        key: {
                            name: 'x_2089324_omnicare_authority_document'
                        }
                    },
                    {
                        table: 'sys_documentation'
                        id: 'e620dd9ec1c3496e95bf002f8072e7a9'
                        key: {
                            name: 'x_2089324_omnicare_citation_control'
                            element: 'title'
                            language: 'en'
                        }
                    },
                    {
                        table: 'sys_dictionary'
                        id: 'ebd6fe4e8f904ee0ab902613cd493d42'
                        key: {
                            name: 'x_2089324_omnicare_citation_control'
                            element: 'NULL'
                        }
                    },
                ]
            }
        }
    }
}
