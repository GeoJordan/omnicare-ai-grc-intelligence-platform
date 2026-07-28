import { Table } from '@servicenow/sdk/core';

export const x_2089324_omnicare_authority_document = Table({
    name: 'x_2089324_omnicare_authority_document',
    label: 'Authority Document',
    attributes: {
        name: {
            type: 'string',
            label: 'Name',
            max_length: 100,
            required: true,
            display: true
        },
        framework_id: {
            type: 'string',
            label: 'Framework ID',
            max_length: 50,
            required: true
        },
        description: {
            type: 'string',
            label: 'Description',
            max_length: 1000
        }
    }
});
