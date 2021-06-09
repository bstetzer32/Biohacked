import React, { useState, useEffect } from "react";
import {Link, useParams} from 'react-router-dom'
import { useDispatch, useSelector } from "react-redux";
import ExerciseTile from "./ExerciseTile";
import { makeStyles } from '@material-ui/core/styles';
import {Card, CardContent, Button, Typography } from '@material-ui/core';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardActions from '@material-ui/core/CardActions';
import CardMedia from '@material-ui/core/CardMedia';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faArrowLeft } from '@fortawesome/free-solid-svg-icons'


const useStyles = makeStyles((theme) => ({
    root: {
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
    },
    card: {
        display: 'flex',
        flexDirection: 'row',
        justifyContent: 'space-between',
        alignItems: 'center',
        width: "80%",
        padding: '2.5%',
        margin: '2.5%',
    },
    button: {
        display: 'flex',
        margin: '2.5%',
        flexDirection: 'column',

    }
}))

export default function WorkoutPage() {
    const { id, workoutId }  = useParams();
    const routines = useSelector(state => state.session.user.routines)
    const routine = routines.find(routine => routine.id === parseInt(id))
    const workout = routine.workouts.find(workout=> workout.id === parseInt(workoutId))
    const classes = useStyles()


    return (
        <div className={classes.root}>
            <Card className={classes.card}> 
                <Link to={`/routines/${id}`} className={classes.back}>
                    <Button>
                        <FontAwesomeIcon icon={faArrowLeft}/>
                        <Typography variant="button">Back</Typography>
                    </Button>
                </Link> 
                <Typography variant="h4">Day {workout.order}</Typography>
                <Button disabled></Button>
            </Card>
            {workout.exercises.map((exercise, i) => <ExerciseTile exercise={exercise} key={`exercise${i}`}/>) }
        </div>
    )
}