import { Component, OnInit } from '@angular/core';
import { ComprehendService } from '../comprehend.service';
import { VoiceRecognitionService } from '../voice-recognition.service'

  export interface IResponse{
    success:boolean,
    response:any
  }

@Component({
  selector: 'app-speech-to-text',
  templateUrl: './speech-to-text.component.html',
  styleUrls: ['./speech-to-text.component.css'],
  providers: [VoiceRecognitionService]
})
export class SpeechToTextComponent implements OnInit {

  keyPhrases!: any;
  entities!: any;
  data!: any;


  formattedKeyPhrases: any;
  formattedEntity: any;

  constructor(
    public service : VoiceRecognitionService,
    private comprehend: ComprehendService
  ) { 
    this.service.init()
   }

  ngOnInit(): void {
  }

  startService(){
    this.service.start()
  }

  stopService(){
    this.service.stop()
    this.comprehend.getKeyPhrases(this.service.text).subscribe((data: { entities: any; keyPhrases: any; data: any; })=> {
      this.entities = data.entities.map((e: { Text: any; }) => e.Text)
      //console.log("ENTITIES",this.entities)
      this.keyPhrases = data.keyPhrases;
      this.data = data.data;
    })

    //console.log("testtt",this.service.text);
    //this.entities.map((entity: any) => {
      
      //find me the weather in Beirut"
      // let startOffset = entity.begin;
      // let endOffset = entity.end

      // this.keyPhrases.substring(0, startOffset -1);  //find me the weather in"

      // this.formattedKeyPhrases.push(this.keyPhrases);
      // this.formattedEntity.push(this.entities);
    //})
 
    }
  }