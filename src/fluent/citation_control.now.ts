import { Table } from '@servicenow/sdk/core';
import { x_2089324_omnicare_authority_document } from './authority_document.now';

export const x_2089324_omnicare_citation_control = Table({
    name: 'x_2089324_omnicare_citation_control',
    label: 'Citation Control',
    attributes: {
        authority_document: {
            type: 'reference',
            label: 'Authority Document',
            reference: x_2089324_omnicare_authority_document,
            required: true
        },
        citation_id: {
            type: 'string',
            label: 'Citation ID',
            max_length: 50,
            required: true,
            display: true
        },
        title: {
            type: 'string',
            label: 'Title',
            max_length: 255,
            required: true
        },
        description: {
            type: 'string',
            label: 'Description',
            max_length: 2000
        }
    }
});
