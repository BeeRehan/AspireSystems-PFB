import React, { Component } from 'react'
import {mobileOperators} from './constant'

const tableHead = Object.keys(mobileOperators[0]);
class TdData extends Component {
  render() {
    return (
        <tbody>
            {
                mobileOperators.map((opr,id)=>{
                    return(
                        <tr key={id}>
                            <td>{opr.rank}</td>
                            <td>{opr.operator}</td>
                            <td>{opr.subscriber}</td>
                            <td>{opr.market_share}</td>
                        </tr>
                    )
                  })
            }
        </tbody>
    )
  }
}

export default class MobileOprator extends Component {
  render() {
    return (
      <div>Mobile Oprator
        <table>
            <thead>
                <tr>
                {
                    tableHead.map((key,id)=>{
                        return(
                            <th key={id}>{key.toUpperCase()}</th>
                            )
                        })
                    }
                    </tr>
            </thead>
            <TdData/>
        </table>
      </div>
    )
  }
}
