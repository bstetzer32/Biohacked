import React, { useState, useEffect } from "react";
import {Link, useParams} from 'react-router-dom'
import { useDispatch, useSelector } from "react-redux";
import ExerciseTile from "./ExerciseTile";
import { makeStyles } from '@material-ui/core/styles';
import {Card, CardContent, IconButton, Typography } from '@material-ui/core';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardActions from '@material-ui/core/CardActions';
import CardMedia from '@material-ui/core/CardMedia';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faPlusCircle } from '@fortawesome/free-solid-svg-icons'


const useStyles = makeStyles((theme) => ({
    root: {
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
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
            {workout.exercises.map((exercise, i) => <ExerciseTile exercise={exercise} key={`exercise${i}`}/>) }
        </div>
    )
}