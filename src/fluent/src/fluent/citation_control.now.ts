import {
  Table,
  StringColumn,
  ReferenceColumn,
} from '@servicenow/sdk/core'

export const x_2089324_omnicare_citation_control = Table({
  name: 'x_2089324_omnicare_citation_control',
  label: 'Citation Control',
  display: 'citation_id',

  schema: {
    authority_document: ReferenceColumn({
      label: 'Authority Document',
      referenceTable: 'x_2089324_omnicare_authority_document',
      mandatory: true,
    }),

    citation_id: StringColumn({
      label: 'Citation ID',
      maxLength: 50,
      mandatory: true,
    }),

    title: StringColumn({
      label: 'Title',
      maxLength: 255,
      mandatory: true,
    }),

    description: StringColumn({
      label: 'Description',
      maxLength: 1000,
    }),
  },
})
