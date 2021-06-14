import React, { useState, useEffect } from "react";
import { BrowserRouter, Route, Switch, Link } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import LoginForm from "./components/auth/LoginForm";
import SignUpForm from "./components/auth/SignUpForm";
import NavBar from "./components/NavBar";
import ProtectedRoute from "./components/auth/ProtectedRoute";
import RoutinesPage from "./components/RoutinesPage";
import RoutinePage from "./components/RoutinePage";
import WorkoutPage from "./components/WorkoutPage";
import ResultsPage from "./components/ResultsPage"
import ResultPage from "./components/ResultPage"
import Questionnaire from './components/Questionnaire'
import RoutineResultsPage from "./components/RoutineResultsPage";
import { authenticate } from "./store/session";
import { Typography, Card } from "@material-ui/core";

function App() {
  useSelector(state => state.session.user)
  const [loaded, setLoaded] = useState(false);
  const dispatch = useDispatch();

  useEffect(() => {
    (async() => {
      await dispatch(authenticate());
      setLoaded(true);
    })();
  }, [dispatch]);

  if (!loaded) {
    return null;
  }

  return (
    <BrowserRouter>
      <NavBar >
      <Switch>
        <Route path="/login" exact={true}>
          <LoginForm />
        </Route>
        <Route path="/sign-up" exact={true}>
          <SignUpForm />
        </Route>
        <ProtectedRoute path="/routines" exact={true} >
          <RoutinesPage/>
        </ProtectedRoute>
        <ProtectedRoute path="/results" exact={true} >
          <ResultsPage/>
        </ProtectedRoute>
        <ProtectedRoute path="/results/:id/result/:resultId">
          <ResultPage/>
        </ProtectedRoute>
        <ProtectedRoute path="/results/:id" exact={true} >
          <RoutineResultsPage/>
        </ProtectedRoute>
        <ProtectedRoute path="/routines/:id/workouts/:workoutId">
          <WorkoutPage/>
        </ProtectedRoute>
        <ProtectedRoute path="/routines/:id">
          <RoutinePage/>
        </ProtectedRoute>
        <ProtectedRoute path="/questionnaires" exact={true} >
          <Questionnaire />
        </ProtectedRoute>
        <ProtectedRoute path="/" exact={true} >
          <Card>
            <Typography variant="h5">
              Welcome to the Biohacked Fitness App.
              </Typography>
              <Typography variant="body1">
              This is a health and wellness app that builds customized workout routines from the results of a questionnaire, tracks results of said questionnaire, and intelligently progresses load every time you record.
              <br/>
              <br/>
              Proceed to <Link to='/routines'>Routines</Link> to fill out a questionnaire and receive a peronalized workout.
            </Typography>
          </Card>
        </ProtectedRoute>
      </Switch>
      </NavBar>
    </BrowserRouter>
  );
}

export default App;
