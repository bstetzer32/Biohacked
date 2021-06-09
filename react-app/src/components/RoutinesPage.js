import React, {  } from "react";
import {Link} from 'react-router-dom'
import { useSelector } from "react-redux";
import RoutineTile from "./RoutineTile";
import { makeStyles } from '@material-ui/core/styles';
import {Card, CardContent, IconButton, Typography } from '@material-ui/core';
// import CardActionArea from '@material-ui/core/CardActionArea';
// import CardActions from '@material-ui/core/CardActions';
// import CardMedia from '@material-ui/core/CardMedia';
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

export default function RoutinesPage() {
  const user = useSelector(state => state.session.user)
  const routines = user.routines
  const classes = useStyles()


    return (
        <div className={classes.root}>
            {routines.length ? routines.map((routine, i) => <RoutineTile routine={routine} key={`routine${i}`}/>) :
            <Card>
                <CardContent>
                    <Typography variant='subtitle1'>
                        This is where your workout routines will appear. To create a routine, click below.
                    </Typography>
                </CardContent>
            </Card>}
            
            <Card className={classes.button}>
                <Link to='/questionnaires'>
                    <IconButton>
                        <FontAwesomeIcon icon={faPlusCircle}/>
                        <Typography variant='button'>Create Routine</Typography>
                    </IconButton>
                </Link>
            </Card>
        </div>
    )
}