import React from 'react'
import Apipage from './Apipage';
import {Table} from '../comps/styles/style.js';

export default function Result() {
    return (
        <div>
            <h1>Appoinment Details</h1>
            <Table>
                <table>
                <thead>
                <tr>
                    <th>ID</th>
                    <th>Doctor</th>
                    <th>Date</th>
                    <th>Reason</th>
                    <th>Status</th>
                </tr>
                </thead>
                <tbody>
                <Apipage/>
                </tbody>
                </table>
            </Table>
        </div>
    )
}
