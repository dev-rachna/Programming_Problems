const event=require('events')

const myEmitter=new event.EventEmitter()


//listen to event - once event occurs call callback
myEmitter.on('someEvent',function(message){
console.log(message,'evnt occured');
})

//trigger Event
myEmitter.emit('someEvent','this is how we trigger event')

