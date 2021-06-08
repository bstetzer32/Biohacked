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
        // width: "80%",
        height: "100%",
        margin: ".5%",
        padding: ".5%"
    }
}))

export default function WorkoutTile({workout, id}) {
    const classes = useStyles()

    return (
        <Card className={classes.root}>
            <Typography>Day {workout.order}</Typography>
            <CardActions>
                <Link to={`/routines/${id}/workouts/${workout.id}`}>
                    <Button>
                        <Typography variant="button">Start Workout</Typography>
                        <div/>
                        <FontAwesomeIcon icon={faDumbbell}/>
                    </Button>
                </Link>
            </CardActions>
        </Card>
    )
}