import React, { } from "react";
import {Link, useParams} from 'react-router-dom'
import { useSelector } from "react-redux";
import ResultTile from "./ResultTile";
import { makeStyles } from '@material-ui/core/styles';
import {Card, Button, Typography } from '@material-ui/core';
// import CardActionArea from '@material-ui/core/CardActionArea';
// import CardActions from '@material-ui/core/CardActions';
// import CardMedia from '@material-ui/core/CardMedia';
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

export default function ResultPage() {
    const { id, resultId }  = useParams();
    const routines = useSelector(state => state.session.user.routines)
    const routine = routines?.find(routine => routine.id === parseInt(id))
    const sets = routine?.results.find(result=> result.id === parseInt(resultId))
    const classes = useStyles()
    const exercises = {}
    sets.results.forEach(set => {
        if (!(set.exercise.id in exercises)) {
            exercises[set.exercise.id] = set.exercise
            exercises[set.exercise.id].sets = []
            exercises[set.exercise.id].sets.push(set)
        } else {
            exercises[set.exercise.id].sets.push(set)
        }
    });
    const results = []
    for (const id in exercises) {
        if (Object.hasOwnProperty.call(exercises, id)) {
            const element = exercises[id];
            results.push(element)
        }
    }


    return (
        <div className={classes.root}>
            <Card className={classes.card}> 
                <Link to={`/results/${id}`} className={classes.back}>
                    <Button>
                        <FontAwesomeIcon icon={faArrowLeft}/>
                        <Typography variant="button">Back</Typography>
                    </Button>
                </Link> 
                <Typography variant="h4">{sets.order}</Typography>
                <Button disabled></Button>
            </Card>
            {results.map((result, i) => <ResultTile exercise={result} key={`result-tile${result.id}`}/>)}
        </div>
    )
}