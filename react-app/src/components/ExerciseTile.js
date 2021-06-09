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
        height: "100%",
        margin: "2.5%",
        padding: "2.5%"
    }
}))

export default function ExerciseTile({exercise}) {
    const classes = useStyles()
    const scheme = exercise.scheme
    const sets = {}
    for (let i = 0; i < scheme.sets; i++) {
        if (scheme.name === "Warmup") {

        }
        
    }

    return (
        <Card className={classes.root}>
            <Typography variant="h6">
                {exercise.scheme.name !== 'Core Dynamic' && exercise.movement !== 'High Intensity Interval Training' && exercise.scheme.name !== 'Warmup' && exercise.scheme.name !== 'Stretch' && exercise.modality.slice(0,1).toUpperCase()}{exercise.scheme.name !== 'Core Dynamic' && exercise.movement !== 'High Intensity Interval Training' && exercise.scheme.name !== 'Warmup' && exercise.scheme.name !== 'Stretch' && exercise.modality.slice(1)} {exercise.movement}
            </Typography>
            <Typography>
                Sets: {exercise.scheme.sets}
            </Typography>
            <Typography>
                {exercise.scheme.reps && `Reps: ${exercise.scheme.reps}`}
            </Typography>
            <Typography>
                {exercise.scheme.tempo && `Tempo: ${exercise.scheme.tempo}(Eccentric, Isometric, Concentric)`}
            </Typography>
            <Typography>
                {exercise.scheme.time && `Work: ${exercise.scheme.time}s`}
            </Typography>
            <Typography>
                {exercise.scheme.rest && `Rest: ${exercise.scheme.rest}s`}
            </Typography>
            <CardActions>
            </CardActions>
        </Card>
    )
}