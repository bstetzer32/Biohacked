import React, { useState } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import {useHistory} from 'react-router-dom'
import { useSelector, useDispatch } from "react-redux";
import {sendQuestionnaire} from "../store/routines";
import {FormControl, FormLabel, RadioGroup, FormControlLabel, Button, Radio, Paper, TextField, Typography, Modal } from '@material-ui/core';
import { authenticate } from "../store/session";

const useStyles = makeStyles((theme) => ({
    root: {
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        padding: '2.5%'
    },
    form: {
        display: 'flex',
        flexDirection: 'column',
    },
    control: {
        display: 'flex',
        padding: '2.5%',
        flexDirection: 'column',

    },
    button: {
        display: 'flex',
        margin: '2.5%',
        alignSelf: 'center',

    },
    modal: {
        top: "40%",
        left: "40%"
    },
    paper: {
        position: "absolute",
        width: "20%",
        minHeight: "20%",
        backgroundColor: theme.palette.background.paper,
        padding: "2.5%",
        top: "30%",
        left: "30%",
    }
}))

export default function Questionnaire() {
    const [parq1, setParq1] = useState('')
    const [parq2, setParq2] = useState('')
    const [parq3, setParq3] = useState('')
    const [parq4, setParq4] = useState('')
    const [parq5, setParq5] = useState('')
    const [parq6, setParq6] = useState('')
    const [parq7, setParq7] = useState('')
    const [barbell, setBarbell] = useState('')
    const [dumbbell, setDumbbell] = useState('')
    const [cable, setCable] = useState('')
    const [lever, setLever] = useState('')
    const [goal, setGoal] = useState('')
    const [height, setHeight] = useState('')
    const [weight, setWeight] = useState('')
    const [age, setAge] = useState('')
    const [errors, setErrors] = useState([])
    const [open, setOpen] = useState(false);

    const handleOpen = () => {
        setOpen(true);
    };

    const handleClose = () => {
        setOpen(false);
        setErrors([])
    };
    const classes = useStyles()
    const user = useSelector(state => state.session.user)
    const dispatch = useDispatch()
    const history = useHistory()

    const onSubmit = (e) => {
        e.preventDefault();
        let errorsExist = false
        if (!parq1  ||
            !parq2 ||
            !parq3 ||
            !parq4 ||
            !parq5 ||
            !parq6 ||
            !parq7 ||
            !barbell||
            !dumbbell||
            !cable||
            !lever||
            !goal) {
            setErrors(["Please choose an option for each select field."])
            errorsExist = true
        }
        if (
          parq1 === "yes" ||
          parq2 === "yes" ||
          parq3 === "yes" ||
          parq4 === "yes" ||
          parq5 === "yes" ||
          parq6 === "yes" ||
          parq7 === "yes"
        ) {
          setErrors((prevErrors) => [
            ...prevErrors,
            "You answered yes to one of the first seven questions. Our system is not capable of recommending a workout for you at this time, as we would require your doctor's approval and stipulations.",
          ]);
          errorsExist = true;
        }
        if (parseInt(age) > 69) {
            setErrors((prevErrors)=> ([...prevErrors, "You answered that you are over the age of 69."]))
            errorsExist = true
        }
        if (errorsExist) {
            handleOpen()
            return
        }
        // if (errors.length) {
        //     setErrors((prevErrors)=> ([...prevErrors, "In order to ensure your health and safety and in accordance with the National Academy of Sports Medicine's scope of practice for certified personal trainers, we cannot provide a workout to you at this time."]))
        //     handleOpen()
        //     return
        // }
        // console.log((parq1 || parq2 || parq3 || parq4 || parq5 || parq6 || parq7) === 'yes', errors)
        const questionnaire = {
            user_id: user.id,
            parq1,
            parq2,
            parq3,
            parq4,
            parq5,
            parq6,
            parq7,
            barbell,
            dumbbell,
            cable,
            lever,
            goal,
            height,
            weight,
            age
        }
        dispatch(sendQuestionnaire(questionnaire)).then(
            ()=> {dispatch(authenticate())}
        ).then(()=>history.push('/routines'))
        
    }
    const errorsModal = (<div className={classes.paper} >
                            <ul>{errors.map((error, i)=> {
                                return (<li><Typography key={`error${i}`}variant="subtitle2">
                                    {error}
                                </Typography></li>)
                            })}</ul>
                            <Typography variant="subtitle2">
                                In order to ensure your health and safety and in accordance with the National Academy of Sports Medicine's stated scope of practice for certified personal trainers, we cannot provide a workout to you at this time.
                            </Typography>
                        </div>)


    return (
      <Paper className={classes.root}>
        <form className={classes.form} onSubmit={onSubmit}>
          <FormControl component="fieldset" className={classes.control}>
            <FormLabel component="legend">
              Has your doctor ever said that you have a heart condition and that
              you should only perform physical activity recommended by a doctor?
            </FormLabel>
            <RadioGroup
              name="parq1"
              onChange={(e) => setParq1(e.target.value)}
              value={parq1}
              required
            >
              <FormControlLabel value="yes" control={<Radio />} label="Yes" />
              <FormControlLabel value="no" control={<Radio />} label="No" />
            </RadioGroup>
          </FormControl>
          <FormControl component="fieldset" className={classes.control}>
            <FormLabel component="legend">
              Do you feel pain in your chest when you perform physical activity?
            </FormLabel>
            <RadioGroup
              name="parq2"
              onChange={(e) => setParq2(e.target.value)}
              value={parq2}
              required
            >
              <FormControlLabel value="yes" control={<Radio />} label="Yes" />
              <FormControlLabel value="no" control={<Radio />} label="No" />
            </RadioGroup>
          </FormControl>
          <FormControl
            component="fieldset"
            className={classes.control}
            required
          >
            <FormLabel component="legend">
              In the past month, have you had chest pain when you were not
              performing any physical activity?
            </FormLabel>
            <RadioGroup
              name="parq3"
              onChange={(e) => setParq3(e.target.value)}
              value={parq3}
              required
            >
              <FormControlLabel value="yes" control={<Radio />} label="Yes" />
              <FormControlLabel value="no" control={<Radio />} label="No" />
            </RadioGroup>
          </FormControl>
          <FormControl component="fieldset" className={classes.control}>
            <FormLabel component="legend">
              Do you lose your balance because of dizziness or do you ever lose
              consciousness?
            </FormLabel>
            <RadioGroup
              name="parq4"
              onChange={(e) => setParq4(e.target.value)}
              value={parq4}
              required
            >
              <FormControlLabel value="yes" control={<Radio />} label="Yes" />
              <FormControlLabel value="no" control={<Radio />} label="No" />
            </RadioGroup>
          </FormControl>
          <FormControl component="fieldset" className={classes.control}>
            <FormLabel component="legend">
              Do you have a bone or joint problem that could be made worse by a
              change in your physical activity?
            </FormLabel>
            <RadioGroup
              name="parq5"
              onChange={(e) => setParq5(e.target.value)}
              value={parq5}
              required
            >
              <FormControlLabel value="yes" control={<Radio />} label="Yes" />
              <FormControlLabel value="no" control={<Radio />} label="No" />
            </RadioGroup>
          </FormControl>
          <FormControl component="fieldset" className={classes.control}>
            <FormLabel component="legend">
              Is your doctor currently prescribing any medication for your blood
              pressure or for a heart condition?
            </FormLabel>
            <RadioGroup
              name="parq6"
              onChange={(e) => setParq6(e.target.value)}
              value={parq6}
              required
            >
              <FormControlLabel value="yes" control={<Radio />} label="Yes" />
              <FormControlLabel value="no" control={<Radio />} label="No" />
            </RadioGroup>
          </FormControl>
          <FormControl component="fieldset" className={classes.control}>
            <FormLabel component="legend">
              Do you know of any other reason why you should not engage in
              physical activity?
            </FormLabel>
            <RadioGroup
              name="parq7"
              onChange={(e) => setParq7(e.target.value)}
              value={parq7}
              required
            >
              <FormControlLabel value="yes" control={<Radio />} label="Yes" />
              <FormControlLabel value="no" control={<Radio />} label="No" />
            </RadioGroup>
          </FormControl>
          <FormControl component="fieldset" className={classes.control}>
            <FormLabel component="legend">
              Do you have access to and feel comfortable using a standard
              barbell setup (freeheld, rack, and bench) with our provided
              exercise videos?
            </FormLabel>
            <RadioGroup
              name="barbell"
              onChange={(e) => setBarbell(e.target.value)}
              value={barbell}
              required
            >
              <FormControlLabel
                value="barbell"
                control={<Radio />}
                label="Yes"
              />
              <FormControlLabel value="no" control={<Radio />} label="No" />
            </RadioGroup>
          </FormControl>
          <FormControl component="fieldset" className={classes.control}>
            <FormLabel component="legend">
              Do you have access to and feel comfortable using dumbbells with
              our provided exercise videos?
            </FormLabel>
            <RadioGroup
              name="dumbbell"
              onChange={(e) => setDumbbell(e.target.value)}
              value={dumbbell}
              required
            >
              <FormControlLabel
                value="dumbbell"
                control={<Radio />}
                label="Yes"
              />
              <FormControlLabel value="no" control={<Radio />} label="No" />
            </RadioGroup>
          </FormControl>
          <FormControl component="fieldset" className={classes.control}>
            <FormLabel component="legend">
              Do you have access to and feel comfortable using standard cable
              machines with attatchments (wide-grip, close-grip, rope, D-handle)
              with our provided exercise videos?
            </FormLabel>
            <RadioGroup
              name="cable"
              onChange={(e) => setCable(e.target.value)}
              value={cable}
              required
            >
              <FormControlLabel value="cable" control={<Radio />} label="Yes" />
              <FormControlLabel value="no" control={<Radio />} label="No" />
            </RadioGroup>
          </FormControl>
          <FormControl component="fieldset" className={classes.control}>
            <FormLabel component="legend">
              Do you have access to and feel comfortable using selectorized
              lever equipment (specialized machines with weight stacks that are
              designed for a specific movement and are typically found near the
              entrance to the gym) with our provided exercise videos?
            </FormLabel>
            <RadioGroup
              name="lever"
              onChange={(e) => setLever(e.target.value)}
              value={lever}
              required
            >
              <FormControlLabel value="lever" control={<Radio />} label="Yes" />
              <FormControlLabel value="no" control={<Radio />} label="No" />
            </RadioGroup>
          </FormControl>
          <FormControl component="fieldset" className={classes.control}>
            <FormLabel component="legend">What is your goal?</FormLabel>
            <RadioGroup
              name="goal"
              onChange={(e) => setGoal(e.target.value)}
              value={goal}
              required
            >
              <FormControlLabel
                value="increase"
                control={<Radio />}
                label="Increase Strength/Size"
              />
              <FormControlLabel
                value="decrease"
                control={<Radio />}
                label="Decrease Body Fat"
              />
              <FormControlLabel
                value="maintain"
                control={<Radio />}
                label="Maintenance"
              />
            </RadioGroup>
          </FormControl>
          <div className={classes.control}>
            <FormLabel component="legend">
              What is your current height in inches?
            </FormLabel>
            <TextField
              value={height}
              label="Height"
              name="height"
              type="number"
              onChange={(e) => setHeight(e.target.value)}
              required
            />
          </div>
          <div className={classes.control}>
            <FormLabel component="legend">
              What is your current weight in pounds?
            </FormLabel>
            <TextField
              value={weight}
              label="Weight"
              name="weight"
              type="number"
              onChange={(e) => setWeight(e.target.value)}
              required
            />
          </div>
          <div className={classes.control}>
            <FormLabel component="legend">What is your current age?</FormLabel>
            <TextField
              value={age}
              label="Age"
              name="age"
              type="number"
              onChange={(e) => setAge(e.target.value)}
              required
            />
          </div>
          <Modal className={classes.modal} open={open} onClose={handleClose}>
            {errorsModal}
          </Modal>
          <Button type="submit" className={classes.button} variant="contained">
            Submit
          </Button>
        </form>
      </Paper>
    );
}