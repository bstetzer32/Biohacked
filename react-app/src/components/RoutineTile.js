import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import {Link} from 'react-router-dom'
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

const useStyles = makeStyles((theme) => ({
    root: {
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        height: "100%",
        margin: "2.5%",
        padding: "2.5%"
    }
}))

export default function RoutineTile({routine}) {
    const classes = useStyles()

    return (
        <Card className={classes.root}>
            <Typography>Goal: {routine.questionnaire.goal === "increase" ? "Increase Muscle Strength/Size" : routine.questionnaire.goal === "decrease" ? "Decrease Bodyfat" : "Maintain Fitness Levels"}</Typography>
            <Typography>Barbells: {routine.questionnaire.barbell ? "Yes" : "No"}</Typography>
            <Typography>Dumbbells: {routine.questionnaire.dumbbell ? "Yes" : "No"}</Typography>
            <Typography>Cable Equipment: {routine.questionnaire.cable ? "Yes" : "No"}</Typography>
            <Typography>Lever Equipment: {routine.questionnaire.lever ? "Yes" : "No"}</Typography>
            <Typography>Started On: {routine.created_at}</Typography>
            <CardActions>
                <Link to={`/routines/${routine.id}`}>
                    <Button>
                        <Typography variant="button">Go To Routine</Typography>
                        <div/>
                        <FontAwesomeIcon icon={faDumbbell}/>
                    </Button>
                </Link>
            </CardActions>
        </Card>
    )
}