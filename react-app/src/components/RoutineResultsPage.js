import React, { } from "react";
import {Link, useParams} from 'react-router-dom'
import { useSelector } from "react-redux";
import ResultsTile from "./ResultsTile";
import { makeStyles } from '@material-ui/core/styles';
import {Card, Typography, Button } from '@material-ui/core';
// import CardActionArea from '@material-ui/core/CardActionArea';
// import CardActions from '@material-ui/core/CardActions';
// import CardMedia from '@material-ui/core/CardMedia';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faArrowLeft } from '@fortawesome/free-solid-svg-icons'
// import { faDumbbell } from '@fortawesome/free-solid-svg-icons'


const useStyles = makeStyles((theme) => ({
    root: {
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
    },
    card: {
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        width: "80%",
        padding: '2.5%',
        margin: '2.5%',
    },
    button: {
        display: 'flex',
        margin: '2.5%',
        flexDirection: 'column',

    },
    back: {
        // position: 'absolute',
        // left: "5%"
    }
}))

export default function RoutineResultsPage() {
    const { id }  = useParams();
    const routines = useSelector(state => state.session.user.routines)
    const routine = routines.find(routine => routine.id === parseInt(id))
    const classes = useStyles()


    return (
        <div className={classes.root}>
            <Card className={classes.card}> 
                <Link to={`/results`} className={classes.back}>
                    <Button>
                        <FontAwesomeIcon icon={faArrowLeft}/>
                        <Typography variant="button">Back</Typography>
                    </Button>
                </Link>           
                <Typography>Goal: {routine.questionnaire.goal === "increase" ? "Increase Muscle Strength/Size" : routine.questionnaire.goal === "decrease" ? "Decrease Bodyfat" : "Maintain Fitness Levels"}</Typography>
            <Typography>Barbells: {routine.questionnaire.barbell ? "Yes" : "No"}</Typography>
            <Typography>Dumbbells: {routine.questionnaire.dumbbell ? "Yes" : "No"}</Typography>
            <Typography>Cable Equipment: {routine.questionnaire.cable ? "Yes" : "No"}</Typography>
            <Typography>Lever Equipment: {routine.questionnaire.lever ? "Yes" : "No"}</Typography>
            <Typography>Started On: {routine.created_at}</Typography>
            </Card>
            {routine.results.map((result, i) => <ResultsTile result={result} key={`result${i}`} id={id} />) }
        </div>
    )
}