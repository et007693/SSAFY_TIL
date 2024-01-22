function Start() {
  (async () => {
      const avatar = await REDBRICK.AvatarManager.createDefaultAvatar();
      const camera = WORLD.getObject("MainCamera");
      const followingCamera = avatar.setFollowingCamera(camera);

      const startbtn = GUI.getObject("runnerz_font_start(beb)");
      const scr1 = GUI.getObject("board_normal_large(2cc)");
      const score = GUI.getObject("button_text_large_white_null(394)");
      const scs = GUI.getObject("font_07_success(7ca)");
      const tmr = GUI.getObject("button_icon_light_1(872)");

      avatar.setDefaultController();

  const donuts = [
    WORLD.getObject('dell1'),
    WORLD.getObject('dell2'),
    WORLD.getObject('dell3'),
    WORLD.getObject('dell4'),
    WORLD.getObject('dell5'),
    WORLD.getObject('dell6'),
    WORLD.getObject('dell7'),
    WORLD.getObject('dell8'),
    WORLD.getObject('dell9'),
    WORLD.getObject('dell10'),
    WORLD.getObject('dell11'),
    WORLD.getObject('dell12'),
    WORLD.getObject('dell13'),
    WORLD.getObject('dell14'),
    WORLD.getObject('dell15'),
  ];
  let starCount = 0;
  const scoreGUI = GUI.getObject('score');
  scoreGUI.setText(starCount + '/' + donuts.length);
  donuts.forEach(starObject => {
    avatar.onCollide(starObject, () => {
      handleStarCollision(starObject);
      if (starCount === donuts.length) {
          scoreGUI.setText('Clear');
      }
  });
  function handleStarCollision(starObject) {
    starObject.kill();
    starCount++;
    scoreGUI.setText(starCount + '/' + donuts.length);
  }
  });
});
}