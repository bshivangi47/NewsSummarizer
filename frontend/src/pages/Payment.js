import * as React from "react";
import { Grid } from "@material-ui/core";
import Header from "../pages/PaymentNav";
import Card from "../Components/Card";
import axios from "axios";
import Pagination from "react-js-pagination";
import Button from "@material-ui/core/Button";



const EXTERNAL_URL='http://localhost/callinglambda';




export default function Home() {


    function getFromLambda() {

        const axios = require('axios')
        axios
            .get(EXTERNAL_URL)
            .then(res => {
                alert(res.data.message)

                console.log(res)
            })
            .catch(error => {
                console.error(error)
            })

    }

    return (
        <>
            <Header />
            <div>
                <img src="/images/payment.png" alt="this is car image" />
            </div>
            <div>
                <Button variant="contained" size="medium" color="primary" onClick={getFromLambda}>Pay</Button>
            </div>
        </>
    );
}
