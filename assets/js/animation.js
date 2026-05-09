var taxi = document.getElementById('car'),
    moveLeft = document.getElementById('left'),
    moveRight = document.getElementById('right'),
    moveUp = document.getElementById('up'),
    moveDown = document.getElementById('down'),
    reqID,
    direction;

function changeDirection(arrow) {
  direction = arrow;
}

function startMoving() {
  if (direction === 'right') {
    taxi.style.left = (taxi.offsetLeft += 2) + 'px';
  } else if (direction === 'left') {
    taxi.style.left = (taxi.offsetLeft -= 2) + 'px';
  } else if (direction === 'up') {
    taxi.style.top = (taxi.offsetTop -= 2) + 'px';
  } else if (direction === 'down') {
    taxi.style.top = (taxi.offsetTop += 2) + 'px';
  }
  
  // tells the browser to keep running the car 60 frames per second.
  reqID = window.requestAnimationFrame(startMoving);
}

function stopMoving() {
  // cancel requestAnimationFrame function to stop moving.
  window.cancelAnimationFrame(reqID);
}

// EventListener Mousedown
moveUp.addEventListener('mousedown', function() {
  changeDirection('up');
  startMoving();
});
moveUp.addEventListener('mouseup', stopMoving);

moveDown.addEventListener('mousedown', function() {
  changeDirection('down');
  startMoving();
});
moveDown.addEventListener('mouseup', stopMoving);

moveLeft.addEventListener('mousedown', function() {
  changeDirection('left');
  startMoving();
});
moveLeft.addEventListener('mouseup', stopMoving);

moveRight.addEventListener('mousedown', function() {
  changeDirection('right');
  startMoving();
});
moveRight.addEventListener('mouseup', stopMoving);