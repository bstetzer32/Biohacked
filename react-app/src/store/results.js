const SET_RESULTS = 'results/setResults'
const CLEAR_RESULTS = 'results/clearResults'

export const setResults = (result) => ({
    type: SET_RESULTS,
    payload: result
})

export const clearResults = () => ({
    type: CLEAR_RESULTS,
})

export const getResults = (exercise) => async (dispatch) => {
    const res = {}
    const sets = []
    const scheme = exercise.scheme
    const set_reps = scheme.reps?.split(',')
    for (let i = 0; i < scheme.sets; i++) {
        if (scheme.name.includes('Compound') || scheme.name.includes('Isolated')) {
            const set = {
                reps: parseInt(set_reps[i]),
                load: Math.round((-0.0278 * exercise.max * parseInt(set_reps[i]) + 1.0278 * exercise.max)/5)*5,
                rest: scheme.rest,
                checked: false
            }
            sets.push(set)
            res[i] = set
        }
        if (scheme.name.includes('Stretch') || scheme.name.includes('Static')|| scheme.name.includes('TABATA')) {
            const set = {
                time: scheme.time,
                rest: scheme.rest,
                checked: false
            }
            sets.push(set)
            res[i] = set
        }
        if (scheme.name.includes('Warmup') || scheme.name.includes('Dynamic')) {
            const set = {
                reps: parseInt(set_reps[0]),
                rest: scheme.rest,
                checked: false
            }
            sets.push(set)
            res[i] = set
        }
        if (scheme.name.includes('Cooldown')) {
            const set = {
                time: scheme.time,
                checked: false
            }
            sets.push(set)
            res[i] = set
        }
        
    }

    dispatch(setResults({[exercise.id]:{results:res, sets: sets}}));
    return sets
};

export const sendResults = (results) => async (dispatch) => {
    await fetch(`/api/results`, {
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({  
            results
        })
    });

    return {}
};


const initialState = {}

export default function reducer(state=initialState, action) {
    const prevState = state
    switch (action.type) {
        case SET_RESULTS:
            const newState = {...prevState, ...action.payload}
            return newState
        case CLEAR_RESULTS:
            return {}
        default:
            return state;
    }
}