import React, { useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { makeStyles } from '@material-ui/core/styles';
import { Redirect } from "react-router-dom";
import { login } from "../../store/session";
import { TextField, Button, Card, Typography } from '@material-ui/core';


const useStyles = makeStyles((theme) => ({
    root: {
        display: 'flex',
        flexDirection: "column",
        alignItems:"center"
    },
    form: {
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        width: "80%"
    },
    button: {
        width: '100%',
        margin: '2.5%',
        alignSelf: "center"
    },
    demoButton: {
        width: '80%',
        margin: '2.5%',
        marginTop: '2.5%',
        alignSelf: "center"
    },
    input: {
        width: '100%',
        margin: '0.5%'
    },
    text: {
        margin: '2.5%',
        marginTop: '2.5%',
        alignSelf: "center",
        textAlign:"center"
    },
}))

const LoginForm = () => {
  // const [errors, setErrors] = useState([]);
  const [emailErrors, setEmailErrors] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [passwordErrors, setPasswordErrors] = useState("");
  const user = useSelector(state => state.session.user);
  const dispatch = useDispatch();
  const classes = useStyles()

  const onLogin = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    if (data.errors) {
      // console.log(data.errors)
      data.errors.forEach(error => {
        if (error.includes('email')) {
          setEmailErrors('Email provided not found.')
        }
        if (error.includes('password')) {
          setPasswordErrors('Password was incorrect.')
        }
      });
    }
  };

  const demoLogin = async (e) => {
    e.preventDefault();
    const data = await dispatch(login('demo@aa.io', 'password'));
    if (data.errors) {
      // console.log(data.errors)
      data.errors.forEach(error => {
        if (error.includes('email')) {
          setEmailErrors('Email provided not found.')
        }
        if (error.includes('password')) {
          setPasswordErrors('Password was incorrect.')
        }
      });
    }
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  if (user) {
    return <Redirect to="/" />;
  }

  return (
    <Card className={classes.root}>
      <form onSubmit={onLogin} className={classes.form}>
      <Typography variant='h3'>Log In</Typography>
          <TextField className={classes.input} error={emailErrors !== ''} helperText={!email ? 'Please enter an email' : emailErrors ? emailErrors : null} value={email} label='Email' type='email' onChange={updateEmail} name="email"/>
          <TextField className={classes.input} error={passwordErrors !== ''} helperText={!password ? 'Please enter a password' : passwordErrors ? passwordErrors : null} value={password} label='Password' type='password' onChange={updatePassword} name="password" autoComplete="password"/>
          <Button type="submit" className={classes.button} variant="contained">Login</Button>
      </form>
      <Button type="submit" onClick={demoLogin} className={classes.demoButton} variant="contained">Demo Login</Button>
      <Typography className={classes.text} variant='h5'>
        Welcome to Biohacked!
      </Typography>
      <Typography className={classes.text} variant='subtitle1'>
       This is a health and wellness app that builds customized workout routines from the results of a questionnaire, tracks results of said questionnaire, and intelligently progresses load every time you record.
      </Typography>
    </Card>
  );
};

export default LoginForm;
