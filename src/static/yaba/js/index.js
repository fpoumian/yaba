import foo from './modules/app';
import $ from 'jquery';
import '../less/styles.less';

console.log('Working!');
console.log(`foo value is ${foo}`);

// Remove required attribute for dev/testing
$("input, textarea").removeAttr("required");