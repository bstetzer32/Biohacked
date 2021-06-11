import React, { } from "react";
import {Link, useParams} from 'react-router-dom'
import { useSelector, useDispatch, useStore } from "react-redux";
import ExerciseTile from "./ExerciseTile";
import { makeStyles } from '@material-ui/core/styles';
import {Card, Button, Typography } from '@material-ui/core';
// import CardActionArea from '@material-ui/core/CardActionArea';
// import CardActions from '@material-ui/core/CardActions';
// import CardMedia from '@material-ui/core/CardMedia';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faArrowLeft } from '@fortawesome/free-solid-svg-icons'
import {sendResults} from '../store/results'


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
    const getStore = useStore()
    const dispatch = useDispatch()
    const results = useSelector(state => state.session.results)
    const routine = routines.find(routine => routine.id === parseInt(id))
    const workout = routine.workouts.find(workout=> workout.id === parseInt(workoutId))
    const classes = useStyles()

    const handleSubmit = (e) => {
        e.preventDefault()

        const store = getStore.getState()
        console.log(store.results)
        dispatch(sendResults(store.results))
    }


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
            {workout.exercises.map((exercise, i) => <ExerciseTile exercise={exercise} key={`exercise-tile${exercise.id}`}/>) }
            <Button onClick={handleSubmit}>Senubmit Workout</Button>
        </div>
    )
}