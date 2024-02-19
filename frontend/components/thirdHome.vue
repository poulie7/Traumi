<template>
    <div class="third">
      <h1>nejbližší koncerty</h1>
      <ul class="concertdate">
        <li>datum</li>
        <li>datum</li>
        <li>datum</li>
      </ul>
    </div>
    </template>
    
    <style scoped>
    

.third {
    min-height: 50vh;
    background-color: #F4F4F4;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    color: #373737;
    text-align: justify;
    padding: 3em;
}
p {
    margin: 2em;
    font-size: larger;
    }
.concertdate {
    list-style-type: none;
    padding: 0;
}

.concertdate li {
  color: #373737; 
  padding: 10px;

}
    
    </style>
    <script setup lang="ts">
    </script>