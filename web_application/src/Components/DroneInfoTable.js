import React from 'react'
import { makeStyles } from '@material-ui/core/styles'
import Table from '@material-ui/core/Table'
import TableBody from '@material-ui/core/TableBody'
import TableCell from '@material-ui/core/TableCell'
import TableContainer from '@material-ui/core/TableContainer'
import TableHead from '@material-ui/core/TableHead'
import TableRow from '@material-ui/core/TableRow'
import Paper from '@material-ui/core/Paper'


const useStyles = makeStyles((theme) =>({
  table: {
    minWidth: 650,
  },
  button: {
    margin: theme.spacing(1),
    align: 'center',
  },
}));



export default function SimpleTable(props) {
  const classes = useStyles();
  var rows = props.items
  return (
      <div>
      <TableContainer component={Paper}>
        <Table className={classes.table} aria-label="simple table">
          <TableHead>
            <TableRow>
              <TableCell align="right">ITEM ID</TableCell>
              <TableCell align="right">ITEM X</TableCell>
              <TableCell align="right">ITEM Y</TableCell>
              <TableCell align="right">DESTINATION_X</TableCell>
              <TableCell align="right">DESTINATION_Y</TableCell>
              <TableCell align="right">DRONE ASSIGNED</TableCell>
              <TableCell align="right">STATUS</TableCell>
              <TableCell align="right">TIME</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {rows.map((row) => (
              <TableRow key={row.item_id}>
                <TableCell align="right">{row.item_id}</TableCell>
                <TableCell align="right">{row.item_x}</TableCell>
                <TableCell align="right">{row.item_y}</TableCell>
                <TableCell align="right">{row.destination_x}</TableCell>
                <TableCell align="right">{row.destination_y}</TableCell>
                <TableCell align="right">{row.assigned_drone}</TableCell>
                <TableCell align="right">{row.status}</TableCell>
                <TableCell align="right">{row.time}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </div>
  );
}