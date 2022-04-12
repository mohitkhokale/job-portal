
import {Grid, TextField, InputLabel, Button} from "@mui/material"

const AddCompany=()=>{
    return(
        <form>
            <Grid container spacing={3}>
                <Grid item xs={6}>
                    <InputLabel>Name</InputLabel>
                    <TextField id="standard-basic" label="Enter a Name" variant="standard" />
                </Grid>
                <Grid item xs={6}>
                    <InputLabel>Email</InputLabel>
                    <TextField id="standard-basic" label="Enter a Email" variant="standard" />
                </Grid>
            </Grid>
            <div>
                <Button variant="contained" color="primary">Submit</Button>
            </div>
                

        </form>
        
        
    )
}
export default AddCompany;