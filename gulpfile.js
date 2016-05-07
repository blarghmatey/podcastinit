var gulp        = require('gulp'),
  sass          = require('gulp-sass'),
  gutil         = require('gulp-util'),
  autoprefix    = require('gulp-autoprefixer'),
  minifyCSS     = require('gulp-minify-css'),
  neat          = require('node-neat').includePaths,
  bourbon       = require('node-bourbon').includePaths,
  stylish       = require('jshint-stylish'),
  concat        = require('gulp-concat'),
  jshint        = require('gulp-jshint'),
  uglify        = require('gulp-uglify'),
  coffee        = require('gulp-coffee'),
  rename        = require('gulp-rename'),
  wait          = require('gulp-wait'),
  notify        = require('gulp-notify'),
  include       = require('gulp-include'),
  plumber       = require('gulp-plumber')
  browserSync   = require('browser-sync'),
  imagemin      = require('gulp-imagemin'),
  argv          = require('yargs').argv,
  gulpif        = require('gulp-if'),
  coffee        = require('gulp-coffee'),
  reload        = browserSync.reload;

var paths = {
  'root':         "dist/",
  'js': {
    "src_watch":  "assets/js/**",
    "src":        "assets/js/**.dev.js",
    "dest":       "dist/js/"
  },
  'scss': {
    "src_watch":  "assets/sass/**",
    "src":        "assets/sass/**.dev.scss",
    "dest":       "dist/css/"
  },
  'img': {
    "src_watch":  "assets/img/**/*",
    "src":        "assets/img/**/*",
    "dest":       "dist/img/"
  }
};

// SASS
gulp.task('sass', function(){
  return gulp.src(paths.scss.src)
    .pipe(sass({includePaths: [bourbon,neat], outputStyle: 'expanded', errLogToConsole: true}))
    .pipe(autoprefix('last 2 version', 'safari 5', 'ie 8', 'ie 9', 'opera 12.1', 'ios 6', 'android 4'))
    .pipe(rename(function(path) { path.basename = path.basename.replace('.dev', '') }))
    .pipe(rename({suffix: '.min'}))
    .pipe(minifyCSS())
    .pipe(gulp.dest(paths.scss.dest))
    .pipe(gulpif(argv.notify, notify({onLast: true, message: 'SCSS compiled!'})));
});

// JS
gulp.task('js', function(){
  return gulp.src(paths.js.src)
    .pipe(include())
    .pipe(jshint())
    .pipe(jshint.reporter(stylish))
    .pipe(rename(function(path) { path.basename = path.basename.replace('.dev', '') }))
    .pipe(rename({suffix: '.min'}))
    .pipe(uglify())
    .pipe(gulp.dest(paths.js.dest))
    .pipe(gulpif(argv.notify, notify({onLast: true, message: 'JS linted!'})));
});

//Process Images
gulp.task('img', function() {
  return gulp.src(paths.img.src)
    .pipe(imagemin())
    .pipe(gulp.dest(paths.img.dest))
    .pipe(notify({onLast: true, message: "Images crunched!"}))
});

//Run the tasks listed above
gulp.task('default', function(){
  gulp.start('sass','js');
});

//Watch for changes and reload the page
gulp.task('watch', function(){
  gulp.watch(paths.scss.src_watch, ['sass']);
  gulp.watch(paths.js.src_watch, ['js']);
});

gulp.task('server:dev', function() {
    browserSync({
        server: {
            baseDir: paths.root
        }
    });
});

//Task That Runs the Processes Listed Above
gulp.task('devBuild', ['sass', 'js']);

//Run the Dev Build Task and Then Fire up a Server
//Use the --notify flag to show messages on task completion
gulp.task('dev', ['devBuild', 'server:dev'], function() {
  gulp.watch(paths.scss.src_watch, ['sass']);
  gulp.watch(paths.js.src_watch, ['js']);
});
