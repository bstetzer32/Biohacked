import React, {  } from "react";
// import { useDispatch, useSelector } from "react-redux";
import {Link} from 'react-router-dom'
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
// import CardActionArea from '@material-ui/core/CardActionArea';
import CardActions from '@material-ui/core/CardActions';
// import CardContent from '@material-ui/core/CardContent';
// import CardMedia from '@material-ui/core/CardMedia';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faDumbbell } from '@fortawesome/free-solid-svg-icons'

const useStyles = makeStyles((theme) => ({
    root: {
        display: 'flex',
        flexDirection: 'row',
        justifyContent: 'space-around',
        alignItems: 'center',
        width: "80%",
        padding: '2.5%',
        margin: '2.5%',
        height: "100%",
    }
}))

export default function ResultsTile({result, id}) {
    const classes = useStyles()

    return (
        <Card className={classes.root}>
            <Typography>{result.created_at}</Typography>
            <CardActions>
                <Link to={`/results/${id}/result/${result.id}`}>
                    <Button>
                        <Typography variant="button">See Results</Typography>
                        <div/>
                        <FontAwesomeIcon icon={faDumbbell}/>
                    </Button>
                </Link>
            </CardActions>
        </Card>
    )
}