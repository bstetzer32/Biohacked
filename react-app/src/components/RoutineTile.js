import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faDumbbell } from '@fortawesome/free-solid-svg-icons'

export default function RoutineTile({routine}) {


    return (
        <>
            <FontAwesomeIcon icon={faDumbbell} border/>
        </>
    )
}