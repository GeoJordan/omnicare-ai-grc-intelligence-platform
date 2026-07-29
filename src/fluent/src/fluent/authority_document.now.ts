import '@servicenow/sdk/global'
import { StringColumn, Table } from '@servicenow/sdk/core'

export const x_2089324_omnicare_authority_document = Table({
  name: 'x_2089324_omnicare_authority_document',
  label: 'Authority Document',
  display: 'name',

  schema: {
    name: StringColumn({
      label: 'Name',
      maxLength: 100,
      mandatory: true,
    }),

    framework_id: StringColumn({
      label: 'Framework ID',
      maxLength: 50,
      mandatory: true,
    }),

    description: StringColumn({
      label: 'Description',
      maxLength: 1000,
    }),
  },
})

