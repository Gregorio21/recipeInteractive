'use strict';

const e = React.createElement

class Hello extends React.Component {
    render(){
       return (
        <h1> hello world </h1>
       );
    }
}

const domContainer = document.querySelector('#root');
ReactDOM.render(<Hello />, domContainer);