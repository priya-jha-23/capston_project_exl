Date-04-2025<img src="./motp12ge.png"
style="width:2.84667in;height:2.6618in" /><img src="./ni2llnqg.png"
style="width:6.26805in;height:0.24028in" /><img src="./5g5nhklo.png"
style="width:2.13208in;height:2.03125in" /><img src="./jchmdsjs.png"
style="width:2.10764in;height:2.03319in" />

Task-AWS (Presented by Priya Jha) S3 Bucket Creation & Public Access
Notes : **Step** **1:** **Create** **an** **S3** **Bucket**

> 1\. Go to **S3**in AWS Console,Then Click **Create** **bucket**.
>
> 2\. Enter **Bucket** **Name(priya-exl)**& choose **Region**(by default
> it is Mumbai as selected previously).
>
> 3\. Uncheck **“Block** **all** **public** **access”**.
>
> 4\. Acknowledge warning → Click **Create** **bucket**.
>
> Then add objects:

**Step** **2:** **Make** **Bucket** **Public** **(for** **Object**
**Access)**

> <img src="./taee1m5r.png"
> style="width:0.94714in;height:0.325in" />1. Go to your bucket
> →**Permissions**tab.

Date-04-2025<img src="./ydzbs2wn.png"
style="width:6.26805in;height:0.80833in" /><img src="./fttid42v.png"
style="width:6.26805in;height:0.64236in" /><img src="./2cfuhjfp.png"
style="width:3.10361in;height:0.74583in" /><img src="./vdth1dkr.png"
style="width:3.27764in;height:1.43403in" /><img src="./vnfk2pkj.png"
style="width:3.30625in;height:0.89568in" />

> 2\. Click **Bucket** **Policy**→ Click **Edit**.
>
> <img src="./rhy01ed5.png"
> style="width:1.22122in;height:0.57847in" />3. Then
>
> 4\. In generate steps we need to fill some details:
>
> For all type of permissions (Get ,put, delete, update etc)
>
> Please copy this Bucket ARN from here and paste it into Amazone
> Resource Name(ARN)
>
> …………………………………………………………………………………………..
>
> <img src="./wytwn4p3.png"
> style="width:1.85347in;height:0.81597in" />Then

Date-04-2025<img src="./sksnmmjr.png"
style="width:2.90375in;height:2.35208in" /><img src="./54rb12lf.png"
style="width:1.18403in;height:0.67753in" /><img src="./yh5axzum.png"
style="width:1.18335in;height:0.54514in" />

> 5\. Add below policy to allow public access to **objects**:
>
> After it save changes (done forget to check /\* after your bucket
> name.)
>
> This makes**objects** **public**, not the bucket itself.

**Step** **3:** **Enable** **StaticWebsite** **Hosting**

> 1\. Go to **Properties**tab in the bucket.
>
> 2\. Scroll to **Static** **website** **hosting**→ Click**Edit**.
>
> 3\. Select **“Enable”**.
>
> 4\. Set:
>
> **Index** **document**: index.html
>
> (Optional)**Error** **document**: error.html
>
> <img src="./wqoybn5k.png"
> style="width:6.65764in;height:2.31097in" />5. Click**Save**
> **changes**.

Date-04-2025<img src="./wurmbcmw.png" style="width:1.84in;height:1.2368in" /><img src="./3iu55qf0.png"
style="width:2.10556in;height:1.25689in" /><img src="./k0vtqi1m.png"
style="width:1.7775in;height:1.44236in" />

> Results:afterpasting the link In the browser.

Key points:

Static website hosting gives you a **website** **endpoint**like:
http://priya-exl.s3-website.ap-south-1.amazonaws.com

> That URL only works if:
>
> • weenabled statichosting.
>
> • We willadd a valid **public-read** **bucket** **policy**.
>
> • The uploaded files (like index.html) are accessible.

Step-by-Step: Launch and Set Up EC2 Instance (EXL Dashboard)

**Step1.** **Go** **toEC2** **Dashboard**

> • Open AWS Console → Search for**EC2**.
>
> • Click on**“EC2”**under Services.

**Step** **2.** **Launch** **an** **Instance**

> • Click **"Launch** **Instance"**.
>
> <img src="./nmotmx3l.png"
> style="width:2.79097in;height:1.98889in" />•
>
> • Enter:
>
> o **Name**: priya-exl-apache2

Date-04-2025<img src="./nv24rj4a.png"
style="width:5.80542in;height:2.44028in" /><img src="./i4uu2j0z.png" style="width:4.7in;height:1.97819in" />

**Amazon** **Machine** **Image** **(AMI)**: Select **Ubuntu** **Server**
**22.04** **LTS**(recommended).

**Instance** **type**: Choose t2.micro (Free Tier eligible).

**Key** **pair**: Create or select an existing one
(prita-exl-apache2.pem).

<img src="./xb0plyqf.png"
style="width:4.65556in;height:2.45208in" />**Network** **settings**:

Date-04-2025<img src="./hf2xqj3t.png"
style="width:4.77389in;height:2.23194in" /><img src="./zhjidlmo.png"
style="width:4.48875in;height:2.00417in" /><img src="./bqvpjs0p.png"
style="width:4.68056in;height:2.46528in" />

Add **HTTP** **(port** **80)**and optionally **HTTPS** **(port**
**443)**if using Apache

> • Click **Launch** **Instance**.
>
> • Now connect towsl:
>
> 1\. Added key-pair file into .ssh. 2. Come into ssh directory

Date-04-2025<img src="./34nm4rwo.png"
style="width:3.54611in;height:0.73542in" /><img src="./3ps1k5c1.png"
style="width:3.13167in;height:0.70278in" /><img src="./xii0alym.png"
style="width:4.15625in;height:0.76944in" /><img src="./00rjvy00.png"
style="width:3.88764in;height:1.62639in" />

Put this command to convert remove rw operation to read operation:

Then configure the instance to wsl ubuntu.

> This Chiriya(Bird kind of structure) means itis connected to aws.

**Step3.** **View** **InstanceDetails**

> • Go to **“Instances”**tab.
>
> • Note the **Public** **IPv4address**(e.g., 65.0.32.145).

Check if Apache is Running

**Open** **Apache** **Web** **Page** **in** **Browser**

> • Open your browser.
>
> • Go to:
>
> http://\<your-public-ip\>

Example: http://65.0.32.145

You should see the **Apache2** **Ubuntu** **Default** **Page**. This
confirms Apache is working.

**3.** **Upload** **Your** **Website** **Files** **(Optional)**

Apache serves content from:

To replace the default page:

Date-04-2025<img src="./wdtov2np.png"
style="width:1.76292in;height:0.93333in" /><img src="./vl1axrfg.png"
style="width:1.39542in;height:0.925in" /><img src="./sobjwbbj.png"
style="width:1.51458in;height:0.89556in" /><img src="./dqxxfybg.png" style="width:1.84in;height:1.2368in" /><img src="./q5xywrmq.png"
style="width:2.10556in;height:1.25689in" /><img src="./qbzcy1xt.png"
style="width:1.7775in;height:1.44236in" />

**4.** **Allow** **HTTP** **Access** **in** **EC2** **(if** **not**
**done)**

Go to:

> • AWS Console → **EC2** **Dashboard**
>
> • Select your instance → **Security** **groups**
>
> • Edit **inbound** **rules**:
>
> o Add **HTTP**(port 80)
>
> o Add **HTTPS**(port 443)–optional
>
> o Add **Custom** **TCP** **22**(SSH)

Some results after setting up these all :

Step-by-Step: Install & Set Up MySQL on Ubuntu EC2

Connect to your EC2 instance

ssh -i "prita-exl-apache.pem"
[<u>ec2-user@65.0.32.145</u>](mailto:ec2-user@65.0.32.145)

Then:

Install MySQL Server

Bash command:sudo apt install mysql-server -y

Date-04-2025<img src="./x4jh4xwr.png"
style="width:4.54042in;height:2.62083in" />

Start & Enable MySQL Service

Bash command:

sudo systemctl start mysql

sudo systemctl enable mysql

Loginto MySQL shell

sudo mysql→mysql\>(shell)

Now start working on Aurora and RDS(Create Database)

> <img src="./y3ocwgaq.png"
> style="width:1.99292in;height:1.87917in" /><img src="./lidhxb4c.png"
> style="width:3.76583in;height:2.06944in" />Choose MySQ

Date-04-2025<img src="./hty2m00y.png"
style="width:3.66722in;height:2.23056in" /><img src="./jmbe44ae.png"
style="width:6.26805in;height:2.94444in" />

Our user: Admin

Create Password : ExlDatabase123

<img src="./cpuwoek5.png"
style="width:6.26805in;height:2.92292in" />Allocate storage :

Date-04-2025<img src="./u5od0mdz.png"
style="width:6.26805in;height:0.9875in" /><img src="./qz5gezgm.png"
style="width:6.26805in;height:0.92986in" /><img src="./cz4wg0jy.png"
style="width:6.26805in;height:0.97361in" /><img src="./4jsldz1c.png"
style="width:4.97597in;height:0.37708in" /><img src="./ilvejegp.png"
style="width:5.03125in;height:1.78542in" />

Public access : Yes

Choose vpc: created by you or default.

Choose Zone availability

Now data base created:

Check Inbound:

Correct……..

Nowwork onwsl:

<img src="./j5bxhtfi.png"
style="width:4.98139in;height:1.59167in" />mysql connectedto awsandwsl

Date-04-2025<img src="./yoeb00qx.png"
style="width:2.52597in;height:0.40972in" /><img src="./f0rd1mcd.png"
style="width:1.45125in;height:0.56111in" /><img src="./ozagd00q.png" style="width:3.50167in;height:1.25in" /><img src="./zhhvig1h.png"
style="width:4.00861in;height:0.57292in" /><img src="./k55hixed.png" style="width:4.01in;height:1.60069in" /><img src="./scbpz5jk.png"
style="width:3.58875in;height:0.61389in" /><img src="./arnqgbyd.png"
style="width:6.26805in;height:1.29444in" />

BasicDatabasecreationandmanipulationcommands:

Nowinstall Pythonandthenrunanscriptto checka databaseconnection.

PythonInatallation:

Thisisfinal outputwhichshowsdatabaseconnectedsuccessfully:

Thisisend.

Thank you!
